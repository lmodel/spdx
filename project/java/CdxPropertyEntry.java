package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A property name with an associated value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CdxPropertyEntry  {

  private String type;
  private String cdxPropName;
  private String cdxPropValue;


}