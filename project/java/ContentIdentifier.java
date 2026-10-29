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
  A canonical, unique, immutable identifier
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContentIdentifier extends IntegrityMethod {

  private String contentIdentifierType;
  private URI contentIdentifierValue;


}