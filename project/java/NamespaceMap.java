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
  A mapping between prefixes and namespace partial URIs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NamespaceMap  {

  private String type;
  private URI namespace;
  private String prefix;


}